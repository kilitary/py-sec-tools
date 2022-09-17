rule _Microsoft_Visual_C_v7_0_Basic_NET_isjwdl
{
	meta:
		description = "Microsoft Visual C_ v7_0  Basic _NET"
	strings:
		$a = {FF2500204000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
