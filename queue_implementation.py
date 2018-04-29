def make_queue():
    return []

def enqueue(q, item):
    q.append(item)

def dequeue(q):
    
    return q.pop(0)
    
def size(q):
   return len(q)
    

q = make_queue()
(enqueue(q, 1))
(enqueue(q, 5))
print(size(q))
print(dequeue(q))


def who_wins(m, players):
    counter=0
    while len(players)>m-1:
        remain_queue=make_queue()
        while 1:
            player=dequeue(players)
            counter+=1
            if counter!=m+1:
                enqueue(remain_queue,player)
            else:
                counter=0
            if len(players)==0:
                players=remain_queue[:]
                remain_queue=make_queue()
                break
    return players
        


who_wins(3, ['val', 'hel', 'jam', 'jin', 'tze', 'eli', 'zha', 'lic'])
who_wins(2, ['poo', 'ste', 'sim', 'nic', 'luo', 'ibr', 'sie', 'zhu'])
