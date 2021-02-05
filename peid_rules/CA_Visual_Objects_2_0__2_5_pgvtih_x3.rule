rule _CA_Visual_Objects_2_0__2_5_pgvtih
{
	meta:
		description = "CA Visual Objects 2_0 _ 2_5"
	strings:
		$a = {87FEE80200000098CC5FBB80????00EB02CD2068F4000000E801000000E3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
