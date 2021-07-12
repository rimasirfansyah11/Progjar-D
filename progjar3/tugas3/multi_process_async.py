# from library import download_gambar, get_url_list
import time
import datetime
import socket
from multiprocessing import Process, Pool


TARGET_IP = "0.0.0.0"
TARGET_PORT = 1000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)


def kirim_gambar(image=None):
    if (image is None):
        return False

    #buka gambar dalam format binary
    f = open(image, "rb")
    l = f.read(1024)
    while (l):
        if(sock.sendto(l, (TARGET_IP, TARGET_PORT))):
            l = f.read(1024)
    f.close()


def kirim_semua():
    texec = dict()
    images = ['1.png', '2.png']
    status_task = dict()
    task_pool = Pool(processes=20) #2 task yang dapat dikerjakan secara simultan, dapat diset sesuai jumlah core
    catat_awal = datetime.datetime.now()
    for k in range(len(images)):
        print(f"mengirim {images[k]}")

        #bagian ini merupakan bagian yang mengistruksikan eksekusi fungsi kirim gambar secara multiprocess
        texec[k] = task_pool.apply_async(func=kirim_gambar, args=(images[k],))

    #setelah menyelesaikan tugasnya, dikembalikan ke main process dengan mengambil hasilnya dengan get
    for k in range(len(images)):
        status_task[k]=texec[k].get(timeout=10)

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")
    print("status TASK")
    print(status_task)


#fungsi kirim_gambar akan dijalankan secara multi process
if __name__=='__main__':
    kirim_semua()