// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SentimentApp",
    platforms: [
        .iOS(.v16)
    ],
    products: [
        .executable(name: "SentimentApp", targets: ["SentimentApp"])
    ],
    targets: [
        .target(
            name: "SentimentApp",
            path: "SentimentApp"
        )
    ]
)
