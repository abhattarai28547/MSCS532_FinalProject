import concurrent.futures

def process_graph_parallel(graph, start, goals):
    results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_goal = {executor.submit(graph.a_star, start, goal): goal for goal in goals}
        for future in concurrent.futures.as_completed(future_to_goal):
            goal = future_to_goal[future]
            try:
                result = future.result()
                results.append(result)
            except Exception as exc:
                print(f'{goal} generated an exception: {exc}')
    return results
