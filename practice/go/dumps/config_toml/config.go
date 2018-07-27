package main

import (
    "os"
    "time"
    "net"
    "fmt"
    
    "github.com/naoina/toml"
)

type Config struct {
    Title string
    Owner struct {
        Name string
        Dob  time.Time
    }
    Database struct {
        Server        string
        Ports         []int
        ConnectionMax uint
        Enabled       bool
    }
    Servers map[string]ServerInfo
    Clients struct {
        Data  [][]interface{}
        Hosts []string
    }
}

type ServerInfo struct {
    IP net.IP
    DC string
}

func main() {
    f, err := os.Open("example.toml")
    if err != nil {
        panic(err)
    }
    defer f.Close()
    var config Config
    if err := toml.NewDecoder(f).Decode(&config); err != nil {
        panic(err)
    }

    // then to use the unmarshaled config...
    fmt.Println("IP of server 'alpha':", config.Servers["alpha"].IP)
}
