# CPU modeling sessions

Request `pool="cpu"` and `webrtc=False` when connecting. The account must have
`cpu_engine_pool` enabled. Without effective access the API falls back to the
default GPU pool; a successful connection or pong does not verify CPU placement.
Use server routing logs to verify the selected pool.

The API derives geometry-only mode from the selected pool. No new `geometry_only` argument is required. Use `pool="default"` to
explicitly retain the GPU route; omitting `pool` also uses the default route.
CPU sessions currently have reduced rendering capabilities. Omit rendering
options, and validate the commands and exports your workload requires before
migrating it. Protocol pings alone do not establish geometry or rendering parity.
