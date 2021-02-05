rule _Microsoft_Visual_C__DLL_cuygky
{
	meta:
		description = "Microsoft Visual C__ DLL"
	strings:
		$a = {535657BB01??????8B??2414}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
