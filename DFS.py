# DFS

peta = {'S':set(['B','A']),
         'A':set(['S','B','D']),
         'B':set(['S','A','C']),
         'C':set(['E','B','D']),
         'D':set(['C','A','F']),
         'E':set(['Z']),
         'Z':set(['E']),
         'F':set(['D'])
         }

def dfs(graph, mulai, goal):
    #mengecek semua node
    explored = []
    # mengecek semua jalur
    stack = [[mulai]]

    # kembali ke jalur apabila awal adalah tujuan
    if mulai == goal:
        return "Awal adalah Tujuan"

    # perulangan sampai dengan semua jalur telah diperiksa
    while stack:
        # masukkan antrian paling belakang ke variabel jalur
        jalur = stack.pop(-1)
        # ambil node terakhir dari jalur
        node = jalur[-1]
        # jika node tidak sama dengan tujuan, maka cek apakah node tidak ada di explored
        if node not in explored:
            neighbours = graph[node] #Memasukan semua isi graph node kedalam neighbours
            # buat jalur baru dan
            # masukan ke dalam queue
            for neighbour in neighbours: #Cek semua neighbour dari graph node
                jalur_baru = list(jalur) #Memasukan isi dari varibel jalur ke variabel jalur baru
                jalur_baru.append(neighbour) #update/tambah isi dari jalur baru dengan neighbour
                stack.append(jalur_baru) #update/tambah isi dari stack dengan jalur baru
                # cek neighbour apakah sama dengan tujuan, jika ya maka return jalur baru
                if neighbour == goal:
                    return jalur_baru # kembali ke jalur baru apa bila neighbour benar

            explored.append(node) #update/tambah isi dari explored dengan node

    # dalam kasus ini tidak ada node yg diinputkan
    return "Mohon maaf node yang dipilih tidak ada"


awal = input("Masukan awal: ")
tujuan = input("Masukan Akhir: ")

print(dfs(peta, awal, tujuan))