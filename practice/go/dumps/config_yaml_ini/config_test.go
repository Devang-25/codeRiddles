package main

import (
	"github.com/stretchr/testify/assert"
	"fmt"
	"os"
	"path/filepath"
	"testing"
)

func TestConfig(t *testing.T) {
	filePath, err := filepath.Abs("./tunables_bft.yaml")
	assert.Nil(t, err)
	os.Setenv(TunablesConfigEnv, filePath)
	config := &Config{}
	err = config.LoadTunablesConfig()
	assert.Nil(t, err)
	assert.NotEqual(t, 0, config.Tunables.BftCommittee.Blocksize)
	assert.Equal(t, 49500, config.Tunables.General.BasePort)
	fmt.Println("Baseport:",config.Tunables.General.BasePort)
	fmt.Println("Blocksize:",config.Tunables.BftCommittee.Blocksize)
}
