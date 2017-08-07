def move_disk(fp, tp):
    print "Moving disk from", fp, "to", tp


def move_tower(height, from_p, to_p, with_p):
    if height >= 1:
        move_tower(height - 1, from_p, with_p, to_p)
        move_disk(from_p, to_p)
        move_tower(height - 1, with_p, to_p, from_p)


move_tower(3, "starting pole", "goal pole", "intermediate pole")

