function download(url) {
    // Retrieve the file contents from the URL
    fetch(url)
      .then(response => response.blob())
      .then(blob => {
        // Create an object URL for the blob
        const url = URL.createObjectURL(blob);
        // Create an invisible link element
        var link = document.createElement('a');
        link.style.display = 'none';
        link.href = url;
        // Set the file name
        link.download = url.substring(url.lastIndexOf('/') + 1);
        // Append the link to the document
        document.body.appendChild(link);
        // Click the link to start the download
        link.click();
        // Remove the link from the document
        document.body.removeChild(link);
        // Release the object URL
        URL.revokeObjectURL(url);
      });
  }

download('https://example.com/myfile.txt');