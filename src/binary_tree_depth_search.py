from collections import deque, defaultdict


def read_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    root = int(lines[0].strip())
    edges = [tuple(map(int, line.strip().split(','))) for line in lines[1:]]
    return root, edges


def write_output(file_path, min_depth):
    with open(file_path, 'w') as f:
        f.write(str(min_depth))


def build_adj_list(edges):
    adj_list = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
    return adj_list


def find_min_depth(root, adj_list):
    visited = set()
    queue = deque([(root, 1)])

    while queue:
        node, depth = queue.popleft()
        if node not in visited:
            visited.add(node)
            if len(adj_list[node]) == 1 and node != root:
                return depth
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    queue.append((neighbor, depth + 1))
    return 0


def main(input_file, output_file):
    root, edges = read_input(input_file)
    adj_list = build_adj_list(edges)
    min_depth = find_min_depth(root, adj_list)
    write_output(output_file, min_depth)


if __name__ == "__main__":
    main("../resources/input_binary_tree.txt", "../resources/output_binary_tree.txt")
