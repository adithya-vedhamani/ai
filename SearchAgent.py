class SearchAgent:

    def __init__(self, graph=dict(), start=None, goal=None, status='idle'):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.status = status
        self.queue = []
        self.no_enqueue = 0
   

    def dfs(self):
        if self.goal == None or self.start == None or len(self.graph) < 2:
            return None

        self.no_enqueue = 0
        Final_result = []
        self.queue = [[self.start]]
        flag = 0
        while(len(self.queue) != 0):
            current_path = self.queue.pop(0)
            current_node = current_path[-1]
            if current_node == self.goal:
                flag = 1
                break

            for child_node in self.graph[current_node].children.keys():
                if child_node not in current_path:
                    self.queue.append(current_path + [child_node])
                    self.no_enqueue += 1
            
            self.queue = sorted(self.queue)
            if (len(self.queue) != 0):
                Final_result.append(self.queue[0])
        if (flag == 0):
            return None
        print(Final_result)
        return Final_result
        
        
    def bms(self):
        if self.goal == None or self.start == None or len(self.graph) < 2:
  
            return None
        
        self.no_enqueue = 0
        Final_result = []
        self.queue = [[self.start]]
        
        while(len(self.queue) != 0):
            length = len(self.queue)
            new_extension = []
            
            for k in range(length):
                current_path = self.queue[k]
                current_node = current_path[-1]
                
                # Explore all neighbors systematically
                unvisited_neighbors = [child for child in self.graph[current_node].children.keys() if child not in current_path]
                unvisited_neighbors.sort()  # Sort for systematic exploration
                
                for child in unvisited_neighbors:
                    temp = current_path + [child]
                    new_extension.append(temp)
                    self.queue.append(temp)
                    self.no_enqueue += 1
                    
            new_extension.sort()  # Sort for systematic exploration
            
            Final_result.extend(new_extension)
            self.queue = self.queue[length:]
            self.queue.sort()  # Sort for systematic exploration
        
        return Final_result


    def bfs(self):
        if self.goal == None or self.start == None or len(self.graph) < 2: ## Create a dialog box to notify user
            return None
        self.no_enqueue = 0
        Final_result = []
        self.queue = [[self.start]]
        flag = 0
        goalpath = []
        while(len(self.queue) != 0):
            length = len(self.queue)
            new_extension = []
            for k in range(length):
                current_path = self.queue[k]
                current_node = current_path[-1]
                for child in self.graph[current_node].children.keys() :
                    if child not in current_path:
                        temp = current_path + [child]
                        new_extension.append(temp)
                        self.queue.append(temp)
                        self.no_enqueue += 1
                        if(child == self.goal):
                            flag = 1
                            goalpath = temp
                            print(temp)
                            break
            
            new_extension = sorted(new_extension)
            Final_result.extend(new_extension)
            if (flag == 1):
                break
            self.queue = self.queue[length:]
            self.queue = sorted(self.queue)
        if (flag == 0):
            return None
        index = Final_result.index(goalpath)
        Final_result = Final_result[:index+1]
        print(Final_result)
        return Final_result

    def hc(self):
        if self.goal == None or self.start == None or len(self.graph) < 2:
            return None
        self.no_enqueue = 0
        Final_result = []
        self.queue = [[int(self.graph[self.start].heuristics), self.start]]

        flag = 0
        goal_path = []
        while len(self.queue) != 0:
            sub_list = []
            current_path = self.queue.pop(0)
            choosen_node = current_path[-1]

            if (self.goal == choosen_node):
                goal_path = current_path
                flag = 1
                break
            
            for child_node in self.graph[choosen_node].children.keys():
                if child_node in current_path :
                    continue
                element = current_path + [child_node]
                element[0] = int(self.graph[child_node].heuristics)
                sub_list.append(element)
                self.no_enqueue += 1

            sub_list = sorted(sub_list)
            print(sub_list)
            for elem in sub_list[-1::-1]:
                self.queue.insert(0,elem)

            if (len(self.queue) != 0):
                Final_result.extend([self.queue[0]])

            if (flag == 1):
                break
        if (flag == 0):
            return None
       
        index = Final_result.index(goal_path)
        Final_result = Final_result[:index+1]
        return Final_result


    def bs(self):
        if self.goal == None or self.start == None or len(self.graph) < 2:
            return None
        self.no_enqueue = 0
        B = 3 # Default beam width
        Final_result = []
        self.queue = [[int(self.graph[self.start].heuristics), self.start]]
        flag = 0
        goal_path = []
        
        while len(self.queue) != 0:
            temp_queue = self.queue.copy()
            K = len(temp_queue)
            extension = []
            for i in range(K):
                choosen_path = self.queue.pop(0)
                choosen_node = choosen_path[-1]
                for child_node in self.graph[choosen_node].children.keys():
                    if child_node in choosen_path:  # To avoid tail biting
                        continue 
                    element = choosen_path + [child_node]
                    element[0] = int(self.graph[child_node].heuristics)
                    priority_queue(extension, element)
                    self.no_enqueue += 1

                    if self.goal == child_node:
                        flag = 1
                        goal_path = element

            
            self.queue = extension.copy()
            if flag == 1:
                Final_result.extend(self.queue.copy())
                print(self.queue, goal_path)  
                break
            else:
                self.queue = self.queue[:B].copy()
                Final_result.extend(self.queue.copy())
                print(self.queue, goal_path)  
                
            
            # Kind of dead lock case condition below
            if self.queue == []:
                break

        if flag == 0:
            return None
        index = Final_result.index(goal_path)
        Final_result = Final_result[:index+1]
        print(Final_result)
        return Final_result

    def bb(self):
        if self.goal == None or self.start == None or len(self.graph) < 2:
            return None
        self.no_enqueue = 0
        self.queue = [[0, self.start]]
        Final_result = []
        flag = 0
        goal_node = []
        while len(self.queue) != 0:
            sub_list = []
            current_path =  self.queue.pop(0)
            choosen_node = current_path[-1]
            for child_node in self.graph[choosen_node].children.keys():
                if child_node in current_path:
                    continue
                element = current_path + [child_node]
                element[0] += self.graph[choosen_node].children[child_node]
                
                sub_list.append(element)
                priority_queue(self.queue, element)
                self.no_enqueue += 1

                if self.goal == child_node:
                    flag = 1
                    goal_node = element
                    break
            sub_list = sorted(sub_list)
            for elem in sub_list:
                priority_queue(Final_result, elem)
            if (flag == 1):
                break
            print("-------------")
        if (flag != 1):
            return None
        index = Final_result.index(goal_node)
        Final_result = Final_result[:index+1]
        print(Final_result)
        return Final_result


    def bb_l(self):
        if self.goal == None or self.start == None or len(self.graph) < 2:
            return None
        self.no_enqueue = 0
        self.queue = [[0, self.start]]
        Final_result = []
        flag = 0
        goal_node = []
        while len(self.queue) != 0:
            sub_list = []
            current_path = self.queue.pop(0)
            choosen_node = current_path[-1]
            for child_node in self.graph[choosen_node].children.keys():
                if child_node in current_path:
                    continue
                element = current_path + [child_node]
                # Update weight
                element[0] += self.graph[choosen_node].children[child_node]
                # Update heuristics appropriately
                prev_node = element[-2]
                if prev_node != self.start:
                    element[0] += (self.graph[child_node].heuristics - self.graph[prev_node].heuristics)
                else:
                    element[0] += (self.graph[child_node].heuristics)
                sub_list.append(element)
                self.no_enqueue += 1

                if self.goal == child_node:
                    flag = 1
                    goal_node = element
                    break

            sub_list = sorted(sub_list)
            sub_list2 = sub_list.copy()
            for elem in sub_list2:
                priority_queue(self.queue, elem)  # Priority queue based on custom criteria
            Final_result.extend(sub_list)
            if flag == 1:
                break

        if flag != 1:
            return None
        index = Final_result.index(goal_node)
        Final_result = Final_result[:index + 1]
        print(Final_result)
        return Final_result

        
    def bb_h(self):
        if self.goal == None or self.start == None or len(self.graph) < 2:
            return None
        self.no_enqueue = 0
        self.queue = [[0, self.start]]
        Final_result = []
        flag = 0
        goal_node = []
        while len(self.queue) != 0:
            sub_list = []
            current_path = self.queue.pop(0)
            #print(current_path)
            choosen_node = current_path[-1]
            for child_node in self.graph[choosen_node].children.keys():
                if child_node in current_path:
                    continue
                element = current_path + [child_node]
                # Update weight
                element[0] += self.graph[choosen_node].children[child_node]
                # Update heuristc aptly
                prev_node = element[-2]
                if prev_node != self.start:
                    element[0] += (self.graph[child_node].heuristics - self.graph[prev_node].heuristics)
                else:
                    element[0] += (self.graph[child_node].heuristics)
                priority_queue(self.queue, element)
                sub_list.append(element)
                self.no_enqueue += 1

                if (self.goal == child_node):
                    flag = 1
                    goal_node = element
                    break
                
            sub_list = sorted(sub_list)
            sub_list2 = sub_list.copy()
            for elem in sub_list2:
                priority_queue(sub_list, elem)
            Final_result.extend(sub_list)
            if (flag == 1):
                break
            print("-------------")
        if (flag != 1):
            return None
        index = Final_result.index(goal_node)
        Final_result = Final_result[:index+1]
        print(Final_result)
        return Final_result
        

    def a_star(self):
        if self.goal == None or self.start == None or len(self.graph) < 2:
            return None
        self.no_enqueue = 0
        # Extended list
        visited = {key : 0 for key in self.graph}
        self.queue = [[0, self.start]]
        Final_result = []
        flag = 0
        goal_path = []
        while len(self.queue) != 0:
            sub_list = []
            current_path = self.queue.pop(0)
            choosen_node = current_path[-1]
            for child_node in self.graph[choosen_node].children.keys():
                if child_node in current_path:
                    continue
                if visited[child_node] == 1:
                    continue
                else:
                    visited[child_node] = 1
                element =  current_path + [child_node]
                
                # Update weight
                element[0] += self.graph[choosen_node].children[child_node]
                # Update heuristc aptly
                prev_node = element[-2]
                if prev_node != self.start:
                    element[0] += (self.graph[child_node].heuristics - self.graph[prev_node].heuristics)
                else:
                    element[0] += (self.graph[child_node].heuristics)
                priority_queue(self.queue, element)
                sub_list.append(element)
                self.no_enqueue += 1
                
                if (self.goal == child_node):
                    flag = 1
                    goal_path = element
                    break

            if len(sub_list) == 0:
                continue
            sub_list = sorted(sub_list)
            sub_list2 = sub_list.copy()
            for elem in sub_list2:
                priority_queue(sub_list, elem)
            Final_result.extend(sub_list)

            if (flag == 1):
                break
            print("-------------")
        if (flag != 1):
            return None
        index = Final_result.index(goal_path)
        Final_result = Final_result[:index+1]
        print(Final_result)
        return Final_result
    
    def aostar(self, max_iterations=1000):
        if self.goal == None or self.start == None or len(self.graph) < 2:
            return None
        self.no_enqueue = 0
        # Extended list
        visited = {key: 0 for key in self.graph}
        self.queue = [[0, self.start]]
        Final_result = []
        flag = 0
        goal_path = []
        for _ in range(max_iterations):
            if len(self.queue) == 0:
                break
            sub_list = []
            current_path = self.queue.pop(0)
            choosen_node = current_path[-1]
            for child_node in self.graph[choosen_node].children.keys():
                if child_node in current_path:
                    continue
                if visited[child_node] == 1:
                    continue
                else:
                    visited[child_node] = 1
                element = current_path + [child_node]
                # Update weight
                element[0] += self.graph[choosen_node].children[child_node]
                # Modify heuristic (AO* modification)
                prev_node = element[-2]
                if prev_node != self.start:
                    element[0] += (self.graph[child_node].heuristics - self.graph[prev_node].heuristics)
                else:
                    element[0] += self.graph[child_node].heuristics
                priority_queue(self.queue, element)
                sub_list.append(element)
                self.no_enqueue += 1
                if self.goal == child_node:
                    flag = 1
                    goal_path = element
                    break
            if len(sub_list) == 0:
                continue
            sub_list = sorted(sub_list)
            sub_list2 = sub_list.copy()
            for elem in sub_list2:
                priority_queue(sub_list, elem)
            Final_result.extend(sub_list)
            if flag == 1:
                break
            print("-------------")
        if flag != 1:
            return None
        index = Final_result.index(goal_path)
        Final_result = Final_result[:index + 1]
        print(Final_result)
        return Final_result

    #This code will perform AO* search with the specified max_iterations parameter and return a list of solutions.
    # Instead of stopping the search when a goal is found, continue searching while periodically checking if the goal is still the best solution found so far.
    # Maintain a list of solutions found during the search, and if a new solution with a lower cost is found, update the list.
    # Use a parameter, such as a time limit or a number of iterations, to determine when to stop the search and return the best solution found so far.
        
    def ora(self):
        if self.goal == None or self.start == None or len(self.graph) < 2:
            return None
        self.no_enqueue = 0
        visited = {key: 0 for key in self.graph}
        self.queue = [[0, self.start]]  # Initial cost is 0
        Final_result = []
        flag = 0
        goal_path = []
        while len(self.queue) != 0:
            sub_list = []
            current_path = self.queue.pop(0)
            choosen_node = current_path[-1]
            for child_node in self.graph[choosen_node].children.keys():
                if child_node in current_path:
                    continue
                if visited[child_node] == 1:
                    continue
                else:
                    visited[child_node] = 1
                element = current_path + [child_node]

                # Update weight
                element[0] += self.graph[choosen_node].children[child_node]
                sub_list.append(element)
                self.no_enqueue += 1

                if self.goal == child_node:
                    flag = 1
                    goal_path = element
                    break

            if len(sub_list) == 0:
                continue
            sub_list = sorted(sub_list)
            sub_list2 = sub_list.copy()
            for elem in sub_list2:
                priority_queue(self.queue, elem)
            Final_result.extend(sub_list)

            if flag == 1:
                break
            print("-------------")
        if flag != 1:
            return None
        index = Final_result.index(goal_path)
        Final_result = Final_result[:index + 1]
        print(Final_result)
        return Final_result

    def ora_h(self):
        if self.goal == None or self.start == None or len(self.graph) < 2:
            return None
        self.no_enqueue = 0
        visited = {key: 0 for key in self.graph}
        self.queue = [[self.graph[self.start].heuristics, self.start]]  # Initial cost is the heuristic value
        Final_result = []
        flag = 0
        goal_path = []
        while len(self.queue) != 0:
            sub_list = []
            current_path = self.queue.pop(0)
            choosen_node = current_path[-1]
            for child_node in self.graph[choosen_node].children.keys():
                if child_node in current_path:
                    continue
                if visited[child_node] == 1:
                    continue
                else:
                    visited[child_node] = 1
                element = current_path + [child_node]

                # Update weight
                element[0] += self.graph[choosen_node].children[child_node]
                # Update heuristics appropriately
                prev_node = element[-2]
                element[0] += self.graph[child_node].heuristics  # Add the heuristic value for the child
                if prev_node != self.start:
                    element[0] -= self.graph[prev_node].heuristics  # Subtract the heuristic value of the previous node

                sub_list.append(element)
                self.no_enqueue += 1

                if self.goal == child_node:
                    flag = 1
                    goal_path = element
                    break

            if len(sub_list) == 0:
                continue
            sub_list = sorted(sub_list)
            sub_list2 = sub_list.copy()
            for elem in sub_list2:
                priority_queue(self.queue, elem)
            Final_result.extend(sub_list)

            if flag == 1:
                break
            print("-------------")
        if flag != 1:
            return None
        index = Final_result.index(goal_path)
        Final_result = Final_result[:index + 1]
        print(Final_result)
        return Final_result
    
    def best(self):
        if self.goal == None or self.start == None or len(self.graph) < 2:
            return None
        self.no_enqueue = 0
        # Extended list
        visited = {key: 0 for key in self.graph}
        self.queue = [[0, self.start]]
        Final_result = []
        flag = 0
        goal_path = []
        while len(self.queue) != 0:
            sub_list = []
            current_path = self.queue.pop(0)
            choosen_node = current_path[-1]
            for child_node in self.graph[choosen_node].children.keys():
                if child_node in current_path:
                    continue
                if visited[child_node] == 1:
                    continue
                else:
                    visited[child_node] = 1
                element = current_path + [child_node]
                # Modify heuristic (Best First Search modification)
                element[0] = self.graph[child_node].heuristics
                priority_queue(self.queue, element)
                sub_list.append(element)
                self.no_enqueue += 1
                if self.goal == child_node:
                    flag = 1
                    goal_path = element
                    break
            if len(sub_list) == 0:
                continue
            sub_list = sorted(sub_list)
            sub_list2 = sub_list.copy()
            for elem in sub_list2:
                priority_queue(sub_list, elem)
            Final_result.extend(sub_list)
            if flag == 1:
                break
            print("-------------")
        if flag != 1:
            return None
        index = Final_result.index(goal_path)
        Final_result = Final_result[:index + 1]
        print(Final_result)
        return Final_result


    
def priority_queue(queue, element):
    if len(queue) == 0:
        selected_index = None
        queue.append(element)
    else:
        selected_index = -1
        for i in range(len(queue)):
            if element[0] < queue[i][0]:
                selected_index = i
                break
            elif element[0] > queue[i][0]:
                selected_index = i + 1
                continue
            else:
                if len(element) < len(queue[i]):
                    selected_index = i
                elif len(element) == len(queue[i]):
                    if element[-1] < queue[i][-1]:
                        selected_index = i
                    else:
                        selected_index = i + 1
                        continue
                else:
                    selected_index = i + 1
                break
        queue.insert(selected_index, element)

    
