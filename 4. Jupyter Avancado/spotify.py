from IPython.core.magic import Magics, magics_class, line_magic, line_cell_magic
from IPython.core.magic_arguments import parse_argstring, magic_arguments, argument
from IPython.display import HTML

EMBED_URL = (
    '<div><iframe src="https://open.spotify.com/embed/{type}/{id}"'
    ' width="{width}" height="{height}"'
    ' frameborder="0" allowtransparency="true"'
    ' allow="encrypted-media"></iframe></div>'
)

# Define classe de mágicas
@magics_class
class SpotifyMagics(Magics):
    
    def embed_player(self, fn, line, cell, type_):
        args = parse_argstring(fn, line)
        ids = args.ids or cell.split('\n')
        result = []
        for aid in ids:
            if aid:
                result.append(EMBED_URL.format(
                    type=type_, id=aid,
                    width=args.width, height=args.height
                ))
        return HTML("<br>".join(result))
    
    @magic_arguments()
    @argument("ids", nargs="*", help="Ids de artistas")
    @argument("-w", "--width", type=int, default=360, help="Largura")
    @argument("-h", "--height", type=int, default=180, help="Altura")
    @line_cell_magic
    def artist(self, line, cell=""):
        return self.embed_player(self.artist, line, cell, 'artist')
        
    @magic_arguments()
    @argument("ids", nargs="*", help="Ids de músicas")
    @argument("-w", "--width", type=int, default=300, help="Largura")
    @argument("-h", "--height", type=int, default=80, help="Altura")
    @line_cell_magic
    def track(self, line, cell=""):
        return self.embed_player(self.track, line, cell, 'track')
        
def load_ipython_extension(kernel):
    # Registra mágicas
    kernel.register_magics(SpotifyMagics)
