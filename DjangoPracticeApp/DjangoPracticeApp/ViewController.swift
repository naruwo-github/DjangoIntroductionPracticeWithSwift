//
//  ViewController.swift
//  DjangoPracticeApp
//
//  Created by Narumi Nogawa on 2020/08/19.
//  Copyright © 2020 Narumi Nogawa. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        
        let url: URL = URL(string: "http://127.0.0.1:8000/api/v1/books/")!
        let task: URLSessionTask = URLSession.shared.dataTask(with: url, completionHandler: {(data, response, error) in
            do {
                let jsonData = try JSONSerialization.jsonObject(with: data!, options: JSONSerialization.ReadingOptions.allowFragments)
                print(jsonData)
            }
            catch {
                print(error)
            }
//            print("data: \(String(describing: data))")
//            print("response: \(String(describing: response))")
//            print("error: \(String(describing: error))")
        })
        task.resume()
    }

}

