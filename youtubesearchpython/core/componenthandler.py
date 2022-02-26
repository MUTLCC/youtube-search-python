from typing import Union, List


def getValue(source: dict, path: List[str]) -> Union[str, int, dict, None]:
    value = source
    for key in path:
        if (
            type(key) is str
            and key in value
            or type(key) is not str
            and type(key) is int
            and value
        ):
            value = value[key]
        elif type(key) is str or type(key) is int:
            value = None
            break
    return value


def getVideoId(videoLink: str) -> str:
    if 'youtu.be' in videoLink:
        if videoLink[-1] == '/':
            return videoLink.split('/')[-2]
        return videoLink.split('/')[-1]
    elif 'youtube.com' in videoLink:
        if '&' not in videoLink:
            return videoLink[videoLink.index('v=') + 2:]
        return videoLink[videoLink.index('v=') + 2: videoLink.index('&')]
    else:
        return videoLink

