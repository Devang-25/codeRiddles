# new package

```
cargo new testp --bin


testp
├── Cargo.toml
└── src
    └── main.rs
```

```
cargo new testplib --lib


testplib/
├── Cargo.toml
└── src
    └── lib.rs
```

```
cargo new testpnone --vcs none

testpnone/
├── Cargo.toml
└── src
    └── main.rs
```


# build

```
cargo build --release
cargo build
```

# run

```
# if built with debug / default
./target/debug/hello_cargo

# build with --release flag
./target/release/hello_cargo
```
