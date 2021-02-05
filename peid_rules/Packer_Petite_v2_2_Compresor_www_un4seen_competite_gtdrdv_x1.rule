rule _Packer_Petite_v2_2_Compresor_www_un4seen_competite_gtdrdv
{
	meta:
		description = "Packer_Petite v2_2 Compresor www_un4seen_competite"
	strings:
		$a = {B800?04?006?00????0???????????0000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
