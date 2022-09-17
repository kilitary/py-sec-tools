rule _Imaging_Technology_Graphics_format_pxcyvr
{
	meta:
		description = "Imaging Technology Graphics format"
	strings:
		$a = {494D0000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
