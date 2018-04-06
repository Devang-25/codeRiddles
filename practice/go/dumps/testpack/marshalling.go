package arcops

import (
  "fmt"
  "reflect"
  "crypto/ecdsa"
  "crypto/elliptic"
  "io/ioutil"
  "path"

  // "math"
  "encoding/hex"
  "crypto/rand"
  "crypto/x509"
  "github.com/ethereum/go-ethereum/common/math"
  "encoding/pem"
  // "encoding/gob"
)

func encode(privateKey *ecdsa.PrivateKey, publicKey *ecdsa.PublicKey) (string, string) {
    cwd := GetCWD()
    filename := ""

    x509Encoded, _ := x509.MarshalECPrivateKey(privateKey)
    pemEncoded := pem.EncodeToMemory(&pem.Block{Type: "PRIVATE KEY", Bytes: x509Encoded})

    filename = fmt.Sprintf("ecdsa.pem")
    err1 := ioutil.WriteFile(path.Join(cwd, filename), []byte(pemEncoded), 0644)
    // err1 := ioutil.WriteFile(path.Join(cwd, filename), pemEncoded, 0644)
    CheckErr(err1, 1)

    x509EncodedPub, _ := x509.MarshalPKIXPublicKey(publicKey)
    pemEncodedPub := pem.EncodeToMemory(&pem.Block{Type: "PUBLIC KEY", Bytes: x509EncodedPub})

    filename = fmt.Sprintf("ecdsa.pub")
    err2 := ioutil.WriteFile(path.Join(cwd, filename), []byte(pemEncodedPub), 0644)
    CheckErr(err2, 1)

    return string(pemEncoded), string(pemEncodedPub)
}

func decode(pemEncoded string, pemEncodedPub string) (*ecdsa.PrivateKey, *ecdsa.PublicKey) {
    block, _ := pem.Decode([]byte(pemEncoded))
    x509Encoded := block.Bytes
    privateKey, _ := x509.ParseECPrivateKey(x509Encoded)

    blockPub, _ := pem.Decode([]byte(pemEncodedPub))
    x509EncodedPub := blockPub.Bytes
    genericPublicKey, _ := x509.ParsePKIXPublicKey(x509EncodedPub)
    publicKey := genericPublicKey.(*ecdsa.PublicKey)

    return privateKey, publicKey
}

func decodeFromFile() (*ecdsa.PrivateKey, *ecdsa.PublicKey) {
    filename := ""

    filename = fmt.Sprintf("ecdsa.pem")
    encodedPem, err1 := ioutil.ReadFile(path.Join(GetCWD(), filename))
    CheckErr(err1, 1)
    block, _ := pem.Decode([]byte(encodedPem))
    x509Encoded := block.Bytes
    privateKey, _ := x509.ParseECPrivateKey(x509Encoded)

    filename = fmt.Sprintf("ecdsa.pub")
    encodedPub, err2 := ioutil.ReadFile(path.Join(GetCWD(), filename))
    CheckErr(err2, 1)
    blockPub, _ := pem.Decode([]byte(encodedPub))
    x509EncodedPub := blockPub.Bytes
    genericPublicKey, _ := x509.ParsePKIXPublicKey(x509EncodedPub)
    publicKey := genericPublicKey.(*ecdsa.PublicKey)

    return privateKey, publicKey
}

func TestMarshalling() {
  fmt.Println("\n...initiating marshalling with elliptic.P256()")
  privateKey, _ := ecdsa.GenerateKey(elliptic.P256(), rand.Reader)
  // privateKey, _ := ecdsa.GenerateKey(elliptic.P384(), rand.Reader)
  publicKey := &privateKey.PublicKey

  encPriv, encPub := encode(privateKey, publicKey)

  fmt.Println(encPriv)
  fmt.Println(encPub)

  priv2, pub2 := decode(encPriv, encPub)

  if !reflect.DeepEqual(privateKey, priv2) {
      fmt.Println("Private keys do not match.")
  }
  if !reflect.DeepEqual(publicKey, pub2) {
      fmt.Println("Public keys do not match.")
  }

  fmt.Println(priv2)
  fmt.Println(pub2)

  priv3, pub3 := decodeFromFile()
  fmt.Println(priv3)
  fmt.Println(pub3)

}

// FromECDSA exports a private key into a binary dump.
func FromECDSA(priv *ecdsa.PrivateKey) []byte {
	if priv == nil {
		return nil
	}
	return math.PaddedBigBytes(priv.D, priv.Params().BitSize/8)
}

func checkECDSA() {
  sk, _ := ecdsa.GenerateKey(elliptic.P256(), rand.Reader)
  fmt.Println(hex.EncodeToString(FromECDSA(sk)))
}
