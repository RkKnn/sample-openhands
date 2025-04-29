package main

// scaffold version 1

import (
        "github.com/labstack/echo/v4"
        "github.com/labstack/echo/v4/middleware"
)

func main() {
        e := echo.New()

        // Middleware for CORS, allowing requests from any origin
        e.Use(middleware.CORS())

        // Serve the React app's index page
        e.GET("/", func(c echo.Context) error {
                return c.File("client/public/index.html")
        })

        // Serve the OpenAPI specification
        e.GET("/openapi.yaml", func(c echo.Context) error {
                c.Response().Header().Set(echo.HeaderContentType, "application/x-yaml")
                return c.File("docs/openapi.yaml")
        })

        // Start the server on port 53805, accessible from any host
        e.Logger.Fatal(e.Start("0.0.0.0:53805"))
}
