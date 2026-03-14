import sys, struct, glob, shutil

def patch_relocs():
    patched = 0
    for f in glob.glob("*.obj"):
        outfile = f.replace('.obj', '.o')
        shutil.copy(f, outfile)
        
        with open(outfile, 'rb+') as file:
            file.seek(0)
            if file.read(4) != b'\x7fELF': 
                continue

            file.seek(40) 
            hdr = struct.unpack('<Q I 6H', file.read(24))
            e_shoff, e_shentsize, e_shnum = hdr[0], hdr[5], hdr[6]

            for i in range(e_shnum):
                file.seek(e_shoff + i * e_shentsize)
                shdr = struct.unpack('<I I Q Q Q Q I I Q Q', file.read(64))

                if shdr[1] == 4: 
                    sh_offset, sh_size, sh_entsize = shdr[4], shdr[5], shdr[9]

                    for j in range(0, sh_size, sh_entsize):
                        file.seek(sh_offset + j + 8) 
                        r_info = struct.unpack('<Q', file.read(8))[0]

                        if (r_info & 0xffffffff) == 40:
                            new_info = (r_info & 0xffffffff00000000) | 9
                            file.seek(sh_offset + j + 8)
                            file.write(struct.pack('<Q', new_info))
                            patched += 1

    print(f"Patched {patched} 'type 40' relocations to standard GOTPCREL (9).")

if __name__ == '__main__':
    patch_relocs()