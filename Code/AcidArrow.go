package main

import (
	"fmt"
	"io"
	"image"
	"image/bmp"
	"net/http"
	"os"
)

func init() {
	image.RegisterFormat("bmp", "bmp", bmp.Decode, bmp.DecodeConfig)
}

func main() {
	fileURL := "https://github.com/BuriedButBreathing/AcidArrow/blob/master/Test.bmp"
	err := DownloadFile("Test.bmp", fileUrl)
	if err != nil {
		panic(err)
	}
	fmt.PrintLn("Downloaded: " fileUrl)
}

//DownloadFile will download a url to alocal file. It's efficient because it will write as it downloads and not load the whole file into memory
func DownloadFile(filepath string, url string) error {

	// Get the Data
	resp, err := http.Get(url)
	if err != nil {
		return err
	}
	defer resp.Body.Close()

	// Create the File
	out, err := os.Create(filepath)
	if err != nil {
		return err
	}
	defer out.Close()

	// Write the body to file
	_, err =io.Cody(out, resp.Body)
	return err
}

func image() {
	imgfile, err := os.Open("./img.jpg")

	if err != nil {
			fmt.Println("img.jpg file not found!")
			os.Exit(1)
	}

	defer imgfile.Close()

	// get image height and width with image/jpeg
	// change accordinly if file is png or gif

	imgCfg, _, err := image.DecodeConfig(imgfile)

	if err != nil {
			fmt.Println(err)
			os.Exit(1)
	}

	width := imgCfg.Width
	height := imgCfg.Height

	fmt.Println("Width : ", width)
	fmt.Println("Height : ", height)

	// we need to reset the io.Reader again for image.Decode() function below to work
	// otherwise we will  - panic: runtime error: invalid memory address or nil pointer dereference
	// there is no build in rewind for io.Reader, use Seek(0,0)
	imgfile.Seek(0, 0)

	// get the image
	img, _, err := image.Decode(imgfile)

	fmt.Println(img.At(10, 10).RGBA())
	for y := 0; y < height; y++ {
			for x := 0; x < width; x++ {
					r, g, b, a := img.At(x, y).RGBA()
					fmt.Printf("[X : %d Y : %v] R : %v, G : %v, B : %v, A : %v  \n", x, y, r, g, b, a)
			}
	}

}