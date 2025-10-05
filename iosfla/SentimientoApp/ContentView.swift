import SwiftUI

struct ContentView: View {
    @StateObject private var api = APIService()
    
    var body: some View {
        NavigationView {
            List(api.news) { item in
                VStack(alignment: .leading) {
                    Text(item.title)
                        .font(.headline)
                    Text("Sentimiento: \(item.sentiment)")
                        .font(.subheadline)
                        .foregroundColor(.secondary)
                    Text(item.source)
                        .font(.caption)
                }
            }
            .navigationTitle("Noticias Uruguay")
            .onAppear {
                api.fetchNews()
            }
        }
    }
}
