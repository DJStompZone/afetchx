"""Tests for the afetchx package."""
import os
import json
import asyncio
import pytest
from afetchx.__main__ import fetch_images_async, load_urls_from_json

TEST_URLS = ["https://unsplash.it/256.jpg", "https://unsplash.it/512.jpg"]

@pytest.fixture
def setup_json_file(tmp_path):
    """Fixture to create a test JSON file in a temporary directory."""
    jsonfile = tmp_path / "test_urls.json"
    with open(jsonfile, "w", encoding="utf-8") as f:
        json.dump(TEST_URLS, f)
    return jsonfile  # Return the path to the JSON file

@pytest.mark.asyncio
async def test_fetch_images_async_basic(tmp_path):
    """Test downloading images from a list of URLs."""
    output_dir = tmp_path / "output_basic"
    await fetch_images_async(
        TEST_URLS, output_dir=output_dir, max_connections=2, cooldown=0.1
    )
    saved_files = os.listdir(output_dir)
    assert len(saved_files) == len(TEST_URLS), "All images should be saved."

def test_load_urls_from_json(setup_json_file):
    """Test loading URLs from a JSON file."""
    jsonfile = setup_json_file
    urls = load_urls_from_json(str(jsonfile))
    assert urls == TEST_URLS, "URLs should be loaded correctly."

@pytest.mark.asyncio
async def test_fetch_images_with_filename_format(tmp_path):
    """Test downloading images with a custom filename format."""
    output_dir = tmp_path / "output_formatted"
    filename_formatter = lambda url: "formatted_" + os.path.basename(url)

    await fetch_images_async(
        TEST_URLS,
        output_dir=output_dir,
        max_connections=2,
        cooldown=0.1,
        filename_formatter=filename_formatter,
    )

    saved_files = os.listdir(output_dir)
    expected_filenames = [filename_formatter(url) for url in TEST_URLS]
    assert sorted(saved_files) == sorted(
        expected_filenames
    ), "Filenames should be formatted correctly."

def test_output_dir_creation(tmp_path):
    """Test that the output directory is created if it doesn't exist."""
    test_dir = tmp_path / "non_existent_dir"

    asyncio.run(
        fetch_images_async(
            TEST_URLS, output_dir=test_dir, max_connections=2, cooldown=0.1
        )
    )

    assert os.path.exists(test_dir), "Output directory should be created."
    saved_files = os.listdir(test_dir)
    assert len(saved_files) == len(TEST_URLS), "All images should be saved."
