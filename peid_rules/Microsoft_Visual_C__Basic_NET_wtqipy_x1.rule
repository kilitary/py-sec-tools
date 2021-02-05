rule _Microsoft_Visual_C__Basic_NET_wtqipy
{
	meta:
		description = "Microsoft Visual C_  Basic _NET"
	strings:
		$a = {FF250020????000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
