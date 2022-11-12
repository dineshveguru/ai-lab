def solution(disk, source, destination, auxiliary):
    if disk == 1:
        print(f"move disk 1 from source {source} to destination {destination}")
        return
    solution(disk - 1, source, auxiliary, destination)
    print(f"move disk {disk} from {source} to {destination}")
    solution(disk - 1, auxiliary, destination, source)


disk = int(input("no of disks: "))
source = input("enter source: ")
auxiliary = input("enter auxiliary: ")
destination = input("enter destination: ")
solution(disk, source, auxiliary, destination)
