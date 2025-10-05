import Foundation

struct NewsItem: Identifiable, Codable {
    let id = UUID()
    let title: String
    let sentiment: String
    let source: String
    let date: String
}
