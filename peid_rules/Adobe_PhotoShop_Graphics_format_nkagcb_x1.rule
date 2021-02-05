rule _Adobe_PhotoShop_Graphics_format_nkagcb
{
	meta:
		description = "Adobe PhotoShop Graphics format"
	strings:
		$a = {3842505300010000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
