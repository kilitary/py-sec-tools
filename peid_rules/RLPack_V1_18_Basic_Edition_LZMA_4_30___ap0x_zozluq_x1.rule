rule _RLPack_V1_18_Basic_Edition_LZMA_4_30___ap0x_zozluq
{
	meta:
		description = "RLPack V1_18 Basic Edition _LZMA 4_30_  __ ap0x"
	strings:
		$a = {60E8000000008B2C2483C4048DB5210B00008D9DFF02000033FFE89F0100006A406800}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
