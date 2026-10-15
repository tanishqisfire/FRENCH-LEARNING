from improve import same_group, LIAISON_SOUNDS

def build_grid(ref, heard):
    rows = len(ref) + 1
    cols = len(heard) + 1
    grid = [[0] * cols for _ in range (rows)]

    for i in range(rows):
        grid[i][0] = i

    for j in range(cols):
        grid[0][j] = j

    for i in range(1, rows):
        for j in range(1, cols):
            if same_group(ref[i - 1], heard[j - 1]):
                sub_cost = 0
            else:
                sub_cost = 1
            grid[i][j] = min(
                grid[i - 1][j - 1] + sub_cost,
                grid[i - 1][j] + 1,
                grid[i][j - 1] + 1,)
            

    return grid     


def trace_back(ref, heard, grid):
    i = len(ref)
    j = len(heard)
    steps = []


    while i > 0 or j > 0:
        if i > 0 and j > 0:
            if same_group(ref[i - 1], heard[j - 1]):
                sub_cost = 0
            else:
                sub_cost = 1
            if grid[i][j] == grid[i - 1][j - 1] + sub_cost:
                if sub_cost == 0:
                    label = "match"
                else:
                    label = "substitution"
                steps.append((label, i - 1, j - 1))
                i -= 1
                j -= 1
                continue 

             
        if i > 0 and grid[i][j] == grid[i - 1][j] + 1:
            steps.append(("deletion", i - 1, None))
            i -= 1
        else:
            steps.append(("insertion", None, j - 1))
            j -= 1

    steps.reverse()
    return steps


def summarize_words(steps, ref,  word_ids, word_count):
    problems = [[] for _ in range(word_count)]
    last_ref = 0

    for label, ref_pos, heard_pos in steps:
        if ref_pos is not None:
            last_ref = ref_pos
        if label == "match":
            continue
        if label == "deletion" and ref[ref_pos] in LIAISON_SOUNDS:
            if ref_pos + 1 == len(word_ids) or word_ids[ref_pos + 1] != word_ids[ref_pos]:
                continue
        problems[word_ids[last_ref]].append((label, ref_pos, heard_pos))


    return problems
