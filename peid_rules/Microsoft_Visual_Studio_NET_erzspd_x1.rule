rule _Microsoft_Visual_Studio_NET_erzspd
{
	meta:
		description = "Microsoft Visual Studio _NET"
	strings:
		$a = {FF250020400000000000000000000000000000000000000000000000000000000000000000000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
