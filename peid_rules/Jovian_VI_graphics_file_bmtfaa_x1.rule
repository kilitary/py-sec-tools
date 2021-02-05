rule _Jovian_VI_graphics_file_bmtfaa
{
	meta:
		description = "Jovian VI graphics file"
	strings:
		$a = {5649??????????00}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
