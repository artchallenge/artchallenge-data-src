paintingWidths = [1440, 1080, 750, 720, 480, 320, 240, 144]
paintingMimeType = 'jpg'
nameWidthImage = lambda width: 'w' + str(width) + '.' + paintingMimeType
paintingFiles = list(map(nameWidthImage, paintingWidths)) + ['max.' + paintingMimeType]
indexFileName = '.index'