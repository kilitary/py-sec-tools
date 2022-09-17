rule _Wavelet_compressed_bitmap_ljjven
{
	meta:
		description = "Wavelet compressed bitmap"
	strings:
		$a = {5749}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
