rule _Unknown_SFX_Archive_MRI__sppzds
{
	meta:
		description = "Unknown SFX Archive _MRI_"
	strings:
		$a = {4D5249}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
