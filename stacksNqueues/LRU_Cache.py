from collections import deque
# not done in O(1) tc - optimal solution uses linked list
class LRUCache:
        #queue?
        # remove>1234<add
        # keys and values = hshmap
        # if the key is not in the hmap,return -1 
        # remove key from queue and append it to other side 

        # if key is in the hash map, set the value of the key in hmap
        # append the key 
        # if the len of the queue is greater than the capacity 
        # popleft from the queue
        # delete that popped left key 
        
        # cleaner pseudocode 
        
        # initialize queue, capacity and hashmap
        # get
        # if the key is not in th hmap, we return -1
        # if it is in the hmap , we remove that key from its position in the queue 
        # append it to the front of the queue 
        # return the value of that key from the hashmap

        # put
        #  if the key is in the hmap already, update the value of the key so that its the most recently used 
        #  else, add the key, value pair to the cache 
        # if no. of keys in queue > capacity delete LRU 
        # then popleft from the queue and store it in a variable least_used which is a key
        # use least_used to access the value and del that accessed value to also delete the key 


    def __init__(self, capacity: int):
        self.q = deque() # use q to store the keys the LRU key should be at the back , mru at the front 
        self.hmap = {} 
        self.capacity = capacity 

    def get(self, key: int) -> int:
        if key not in self.hmap:
            return -1 
        else:
            self.q.remove(key) # revise 
            self.q.append(key)
            return self.hmap[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            self.hmap[key] = value
            self.q.remove(key)
            self.q.append(key)
        else:
            self.hmap[key] = value
            self.q.append(key)
            if len(self.q) > self.capacity:
                least_used = self.q.popleft()
                del self.hmap[least_used]

# time and space complexity - o(n)






        # for key, value in self.hmap.keys():
        #     if key,value not in self.hmap.keys():
        #         self.q.append(key)
        #         self.q.append(value)
        #         if self.q.count(key) > capacity:
        #             self.q.popleft()
        #         else:
        #             self.hmap.append(key,value)
        #             self.q.append(key)
        #             self.q.append(value)



        


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
param_1 = obj.get(1)
obj.put(key,value)