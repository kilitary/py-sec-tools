rule _RLPack_Full_Edition_1_17_DLL_LZMA__ghtags
{
	meta:
		description = "RLPack Full Edition 1_17 DLL _LZMA_"
	strings:
		$a = {807C2408010F85????????60E8000000008B2C2483C4048DB55A0A00008D9D4002000033FFE8????????6A4068????????68????????6A00FF95EB0900008985}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
