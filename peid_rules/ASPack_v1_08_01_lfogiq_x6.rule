rule _ASPack_v1_08_01_lfogiq
{
	meta:
		description = "ASPack v1_08_01"
	strings:
		$a = {60EB0A5DEB02FF2545FFE5E8E9E8F1FFFFFFE981ED236A4400BB10??440003DD2B9D72}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
