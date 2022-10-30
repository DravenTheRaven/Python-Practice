class PictureDownload(Thread):
    def __init__(self, url):
        super().__init__()

        self.picture_file = None
        self.url = url

    def run(self):
        """ download a picture and save it to a file """
        # download the picture
        response = requests.get(self.url, proxies=proxyDict)
        picture_name = self.url.split('/')[-1]
        picture_file = f'./assets/{picture_name}.jpg'

        # save the picture to a file
        with open(picture_file, 'wb') as f:
            f.write(response.content)

        self.picture_file = picture_file

class App(tk.TK):
    def __init__(self, canvas_width, canvas_height):
        super().__init__()
        self.resizable(0, 0)
        self.title('Image Viewer')

        # progress frame
        self.progress_frame = ttk.Frame(self)

        #configure the grid to place the progress bar is at the center
        self.progress_frame.rowconfigure(0, weight=1)
        self.pregress_frame.rowconfigure(0, weight=1)

        #progress bar
        self.pb = ttk.Progressbar(
            self.progress_frame, orient=tk.HORIZONTAL, mode='indeterminate')
        self.pb.grid(row=0, column=0, sticky=tk.EW, padx=10, pady=10)

        #place the progress Frame
        self.progress_frame.grid(row=0, column=0, sticky=tk.NSEW)

        #picture Frame
        self.picture_frame = ttk.Frame(self)

        # canvas width &amd; height
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

        #canvas
        self.canvas = tk.Canvas(
            self.picture_frame,
            width=self.canvas_width,
            height=self.canvas_height)
        self.picture_frame.grid(row=0, column=0)

    def handle_download(self):
        """Download a random photo from unsplash """
        self.start_downloading()

        url = 'https://source.unsplash.com/random/640x480'
    download_thread = PictureDownload(url)
    download_thread.start()

    self.monitor(download_thread)
