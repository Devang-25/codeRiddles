/*
Copyright (c) 2018 TrueChain Foundation

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

package main

import (
	"fmt"
	"gopkg.in/ini.v1"
	"gopkg.in/yaml.v2"
	"io/ioutil"
	"log"
	"os"
	"path"
)

const (
	tunablesConfigEnv = "TRUE_TUNABLES_CONF"
	generalConfigEnv  = "TRUE_GENERAL_CONF"
	peerNetworkEnv    = "TRUE_NETWORK_CONF"
	SimulatedEnv      = "TRUE_SIMULATION"
)

// type T struct {
// 	A string
// 	B struct {
// 		RenamedC int   `yaml:"some"`
// 		D        []int //`yaml:"RenamedD"`
// 	}
// 	Ew int `yaml:"eW"`
// 	G  int `yaml:"g"`
// }

type Tunables struct {
	// some_thing is the struct tag, to add metadata to a struct's fields
	// SomeThing int `yaml:"something"`
	// testbed config
	TestbedConfig struct {
		ClientID int `yaml:"client_id"`
		Requests struct {
			Max int `yaml:"max"`
		}
		ThreadingEnabled bool `yaml:"threadingEnabled"`
	}

	// slow chain
	Slowchain struct {
		Csize int `yaml:"csize"`
	}
	General struct {
		BasePort   int `yaml:"basePort"`
		maxLogSize int
	}
}

// Config  configuration for pbft
type Config struct {
	Logistics struct {
		clientLog string
		KD        string // key directory where pub/priva ECDSA keys are stored

	}

	tunables Tunables
	Network  struct {
		N      int      // number of nodes to be launchedt
		IPList []string // stores list of IP addresses belonging to BFT nodes
		Ports  []int    // stores list of Ports belonging to BFT nodes
	}
}

func DefaultTunables() *Tunables {
	return &Tunables{
		SomeThing: 4,
	}
}

// LoadLogisticsCfg loads the .cfg file
func LoadLogisticsCfg() (*ini.File, error) {
	path := os.Getenv(generalConfigEnv)
	if path == "" {
		path = "/etc/truechain/logistics_bft.cfg"
	}
	configData, err := ini.Load(path)
	if err != nil {
		fmt.Printf("Error reading ini file: %v", err)
		return configData, err
	}
	return configData, nil
}

// LoadTunablesConfig loads the .yaml file
func LoadTunablesConfig() error {

	path := os.Getenv(tunablesConfigEnv)
	if path == "" {
		path = "/etc/truechain/tunables_bft.yaml"
	}

	yamlFile, err := ioutil.ReadFile(path)

	if err != nil {
		log.Printf("Unable to read config file. Error:%+v \n", err)
		return err
	}

	// tcfg := make(map[interface{}]interface{})

	// fmt.Println(string(yamlFile))
	tcfg := Tunables{}
	// tcfg := T{}
	err = yaml.Unmarshal(yamlFile, &tcfg)
	if err != nil {
		log.Printf("Unable to Unmarshal config file. Error:%+v", err)
		return err
	}

	fmt.Println("BLABLA1")
	// fmt.Println(tcfg)
	fmt.Printf("--- tcfg:\n%v\n\n", tcfg)
	// testbed := tcfg["testbed_config"]
	// fmt.Println(testbed["threading_enabled"])

	return nil
}

// ValidateConfig checks for aberrance and loads struct Config{} with tunables and logistics vars
// func ValidateConfig(cfgData *ini.File)
func (cfg *Config) ValidateConfig(configData *ini.File) error {
	// TODO: refer to validate yaml from browbeat
	HostsFile := os.Getenv(peerNetworkEnv)
	if HostsFile == "" {
		HostsFile = "/etc/truechain/hosts"
	}
	return nil
}

func CheckErr(err error) {
	if err != nil {
		log.Printf("Error: Validate config file values failed. Error: %+v", err)
	}
}

// GetPbftConfig returns the basic PBFT configuration used for simulation
func GetPbftConfig() *Config {
	cfg := &Config{}
	err := LoadTunablesConfig()

	cfgData, err := LoadLogisticsCfg()
	// CheckErr(err)
	if cfgData != nil {
		cfg.Logistics.KD = cfgData.Section("general").Key("pem_keystore_path").String()
	} else {
		fmt.Println("Unable to find section [general][pem_keystore_path]. Using current folder to store keys.")
		cfg.Logistics.KD = path.Join("./keys/")
	}
	err = cfg.ValidateConfig(cfgData)
	CheckErr(err)
	return cfg
}

func main() {
	cfg := GetPbftConfig()
	fmt.Println(cfg)
}
