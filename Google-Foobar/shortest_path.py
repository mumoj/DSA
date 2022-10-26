from collections import deque
from pprint import pprint

def solution(map):
    
    def bfs (graph, start_node):

        visited = [[None for i in range(0, len(row))] for j,row in enumerate(graph)]
        queue = deque([start_node])
        
        visited[start_node[0]][start_node[1]] = 1

        while queue:
            cx, cy = queue.popleft()

            for x,y in [(0,1),(0,-1), (-1, 0), (1, 0)]:
                nx = cx+x
                ny = cy+y
                
                if 0 <= nx < len(visited):
                    if 0 <= ny < len(visited[nx]) and visited[nx][ny] is None:
                        visited[nx][ny] = visited[cx][cy] + 1
                        if graph[nx][ny] == 0:
                            queue.append((nx, ny))
                        else:
                            pass          
        return visited

    end_x = len(map)-1
    end_y = len(map[end_x])-1

    start_end  = bfs(map, (0,0))
    end_start = bfs(map, (end_x, end_y))

    min_steps = float('inf')
    for j, row in enumerate(map):
        for i in range(0, len(row)):
            if start_end[j][i] and end_start[j][i]:
                min_steps = min(start_end[j][i]+end_start[j][i]-1, min_steps)
    
    return min_steps

             



print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))






        

        



