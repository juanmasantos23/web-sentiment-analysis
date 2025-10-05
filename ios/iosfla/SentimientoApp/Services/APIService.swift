import Foundation

class APIService: ObservableObject {
    @Published var news: [NewsItem] = []
    
    func fetchNews() {
        guard let url = URL(string: "http://TU_SERVIDOR_PUBLICO:5000/news") else { return }
        
        URLSession.shared.dataTask(with: url) { data, _, error in
            if let data = data {
                if let decoded = try? JSONDecoder().decode([NewsItem].self, from: data) {
                    DispatchQueue.main.async {
                        self.news = decoded
                    }
                }
            }
        }.resume()
    }
}
