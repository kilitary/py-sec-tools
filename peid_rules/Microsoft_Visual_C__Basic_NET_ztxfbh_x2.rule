rule _Microsoft_Visual_C__Basic_NET_ztxfbh
{
	meta:
		description = "Microsoft Visual C_  Basic _NET"
	strings:
		$a = {01DB078B1E83EEFC11DBEDB80100000001DB078B1E83EEFC11DB11C001DB730B}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
