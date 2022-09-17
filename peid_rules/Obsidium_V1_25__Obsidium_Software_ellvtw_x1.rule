rule _Obsidium_V1_25__Obsidium_Software_ellvtw
{
	meta:
		description = "Obsidium V1_25 __ Obsidium Software"
	strings:
		$a = {E80E0000008B54240C8382B80000000D33C0C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
