from datasets import load_dataset, VerificationMode
import datetime

dataset = load_dataset(
    "projecte-aina/CA-EN_Parallel_Corpus",
    split="train",
    verification_mode=VerificationMode.NO_CHECKS,
    trust_remote_code=True,
)

print("Dataset loaded")

skip = 0
with open("aina-parallel.en", "w") as fh_source, open(
    "aina-parallel.ca", "w"
) as fh_target, open("aina-parallel.excluded.en", "w") as fh_source_excluded, open(
    "aina-parallel.excluded.ca", "w"
) as fh_target_excluded:
    read = 0
    wrote = 0
    excluded = 0
    for entry in dataset:
        ca = entry["ca"]
        en = entry["en"]
        domain = entry["Domain"]
        read += 1

        if domain in ["PRN"]:
            fh_source_excluded.write(f"{en} - {domain}\n")
            fh_target_excluded.write(f"{ca}\n")
            excluded += 1
            continue

        fh_source.write(f"{en}\n")
        fh_target.write(f"{ca}\n")
        wrote += 1

    print(f"Total read lines: {read}")
    print(f"Total wrote lines: {wrote}")
    print(f"Total excluded lines: {excluded}")
    start_time = datetime.datetime.now()
    s = "Time used: {0}".format(datetime.datetime.now() - start_time)
    print(s)
