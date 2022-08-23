"""
	P05-04: Vertex detector
"""
def get_vertex_count(lst: list) -> int:
	"""
	It takes a list of numbers and returns the number of vertices in the list
	
	:param lst: list
	:type lst: list
	:return: The number of vertices in the list.
	"""
	vertex_count: int = 0
	if len(lst) < 2:
		return vertex_count
	
	for i in range(1, len(lst) - 1):
		if lst[i] > lst[i+1] and lst[i] > lst[i-1]:
			vertex_count += 1
	

	return vertex_count


def main() -> None:
	"""
	It takes a list of integers, and returns the number of vertices in the polygon
	"""
	data_points: list = [int(i) for i in input().split()]
	print(get_vertex_count(data_points))

if __name__ == '__main__':
	main()