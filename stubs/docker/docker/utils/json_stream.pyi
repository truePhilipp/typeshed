from _typeshed import Incomplete
from collections.abc import Generator

json_decoder: Incomplete

def stream_as_text(stream) -> Generator[Incomplete, None, None]: ...
def json_splitter(buffer): ...
def json_stream(stream): ...
def line_splitter(buffer, separator: str = "\n"): ...
def split_buffer(stream, splitter: Incomplete | None = None, decoder=...) -> Generator[Incomplete, None, Incomplete]: ...
