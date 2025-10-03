"""Main game loop for the Hostia retro point-and-click horror prototype."""

from __future__ import annotations

import sys
from dataclasses import dataclass
from typing import Tuple

import pygame


@dataclass
class RetroPalette:
    """Simple 16-color retro palette reminiscent of MS-DOS CGA/EGA."""

    colors: Tuple[Tuple[int, int, int], ...] = (
        (0, 0, 0),  # noir
        (170, 0, 0),  # rouge sombre
        (0, 170, 0),  # vert
        (170, 85, 0),  # marron
        (0, 0, 170),  # bleu
        (170, 0, 170),  # violet
        (0, 170, 170),  # cyan
        (170, 170, 170),  # gris clair
        (85, 85, 85),  # gris foncé
        (255, 85, 85),  # rouge clair
        (85, 255, 85),  # vert clair
        (255, 255, 85),  # jaune
        (85, 85, 255),  # bleu clair
        (255, 85, 255),  # magenta
        (85, 255, 255),  # cyan clair
        (255, 255, 255),  # blanc
    )


class HostiaGame:
    """Minimal skeleton for the Hostia point-and-click game."""

    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Hostia - Prototype 1")
        self.clock = pygame.time.Clock()
        self.palette = RetroPalette()

        # Résolution typique 320x200, mise à l'échelle x3 pour plus de confort
        self.base_resolution = (320, 200)
        self.scale = 3
        self.window_size = (self.base_resolution[0] * self.scale, self.base_resolution[1] * self.scale)
        self.screen = pygame.display.set_mode(self.window_size)

        # Surface interne en basse résolution pour le rendu pixelisé
        self.canvas = pygame.Surface(self.base_resolution)

        # Police système par défaut pour les messages temporaires
        self.font = pygame.font.SysFont("Terminal", 12)

    def run(self) -> None:
        """Execute the main loop until the user closes the window."""

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self._draw_title_screen()
            self._flip_buffers()
            self.clock.tick(30)

        pygame.quit()
        sys.exit()

    def _draw_title_screen(self) -> None:
        """Render a temporary title screen placeholder."""

        self.canvas.fill(self.palette.colors[0])  # noir

        # Cadre simple pour rappeler les interfaces rétro
        border_color = self.palette.colors[7]
        pygame.draw.rect(self.canvas, border_color, self.canvas.get_rect(), 1)

        title_text = self.font.render("HOSTIA", True, self.palette.colors[9])
        subtitle_text = self.font.render("Prototype 1 - Ecran titre temporaire", True, self.palette.colors[14])
        instructions_text = self.font.render("Clique pour continuer (fonctionnalité à venir)", True, self.palette.colors[6])

        # Centre approximatif pour la mise en page rétro
        self.canvas.blit(title_text, title_text.get_rect(center=(160, 80)))
        self.canvas.blit(subtitle_text, subtitle_text.get_rect(center=(160, 110)))
        self.canvas.blit(instructions_text, instructions_text.get_rect(center=(160, 140)))

    def _flip_buffers(self) -> None:
        """Met à l'échelle la surface basse résolution vers la fenêtre."""

        scaled_surface = pygame.transform.scale(self.canvas, self.window_size)
        self.screen.blit(scaled_surface, (0, 0))
        pygame.display.flip()


def main() -> None:
    """Point d'entrée du prototype."""

    game = HostiaGame()
    game.run()


if __name__ == "__main__":
    main()
