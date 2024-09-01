import os
import pygame


def list_of_files(directory: str, extension: str) -> list[str]:
    """
    :param directory: chemin du dossier
    :type directory: str
    :param extension:extension du fichier
    :type extension: str
    :return: files_names: liste des noms des présidents
    """
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


tile_size = 64


def screen_size():

    width = tile_size * 20
    height = tile_size * 10
    return width, height



screen_width, screen_height = screen_size()
screen = pygame.display.set_mode((screen_width, screen_height))
