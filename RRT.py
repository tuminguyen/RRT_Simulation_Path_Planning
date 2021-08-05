from RRTBase import RRTMap, RRTGraph
from cfg import *
import pygame
import argparse


def init_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', '-m', default='easy',
                        type=str, help='scene mode')
    args = parser.parse_args()
    return vars(args)


if __name__ == '__main__':
    pygame.init()
    arguments = init_parse()
    if arguments['mode'] == 'easy':
        LINES = list()
        OUT_TRI_LIST = list()
        OUT_RECT_LIST = list()
    rrt_map = RRTMap(START, TARGET, LINES, OBS_DIM, OBS_NUM, OUT_TRI_LIST, OUT_RECT_LIST)
    rrt_map.draw_map()
    obs = rrt_map.get_obs()
    rrt_graph = RRTGraph(START, TARGET, obs, OUT_TRI_LIST, OUT_RECT_LIST, STEP_SIZE)
    run = True
    count = 0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False
        while not rrt_graph.path_history():
            if count % 5 == 0:
                xs, ys, parents = rrt_graph.bias(TARGET)
                pygame.display.update()
            else:
                xs, ys, parents = rrt_graph.extend()
            pygame.draw.circle(rrt_map.map, rrt_map.red, (xs[-1], ys[-1]), 4, 0)
            pygame.draw.line(rrt_map.map, rrt_map.blue, (xs[-1], ys[-1]),
                             (xs[parents[-1]], ys[parents[- 1]]), 1)
            count += 1
        if rrt_graph.finish_flag:
            path_nodes = rrt_graph.get_path_nodes()
            for pn in path_nodes:
                pygame.draw.circle(rrt_map.map, rrt_map.blue, pn, 4, 0)
            pygame.display.update()
